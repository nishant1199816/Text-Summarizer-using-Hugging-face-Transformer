#  fastapi
from fastapi import FastAPI, Request
from pydantic import BaseModel  # its id use for text inpute
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import re
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# initialize our fastapi app
app = FastAPI(title="Text Summarization App",
              description="Text Summarization using T5", version="1.0")

model = T5ForConditionalGeneration.from_pretrained("./saved_summary_model")
tokenizer = T5Tokenizer.from_pretrained("./saved_summary_model")

# device
if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

model.to(device)

templates = Jinja2Templates(directory=".")

# inpute schema for dialogue => string ki form me hoga , here we are using pydantic for data validation and serialization


class DialogueInput(BaseModel):
    dialogue: str


def clean_data(text):
    text = re.sub(r"\r\n", " ", text)  # lines
    text = re.sub(r"\s+", " ", text)  # spaces
    text = re.sub(r"<.*?>", " ", text)  # html tags <p> <h1>
    text = text.strip().lower()
    return text


def summarize_dialogue(dialogue: str) -> str:
    # clean diaalogue
    dialogue = clean_data(dialogue)

    # tokenize
    inputs = tokenizer(
        dialogue,
        padding="max_length",
        max_length=512,
        truncation=True,
        return_tensors="pt"
    ).to(device)

    # Generate the summary => token ids mein generate karega
    model.to(device)
    targets = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=150,
        num_beams=4,  # its produce 4 outcomes inmei se jo best hoga ushe ye deliver karegaassistant_model=
        early_stopping=True
    )

    # decode our output
    summary = tokenizer.decode(targets[0], skip_special_tokens=True)
    return summary

# Api Endpoint


@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):
    summary = summarize_dialogue(dialogue_input.dialogue)
    return {"summary": summary}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )
