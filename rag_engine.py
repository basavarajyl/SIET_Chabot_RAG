import falss
import numpy as np
from groq import Groq
from pydf import PDFReader
from sentence_transformers import SentenceTransformer
def lode_pdf (pdf_path):
   reader = PDFReader(str(pdf_path))
  mypages = [i.extract_text() or "" for i in reader.pages]
full_text = "\n",join(mypages).strip()
if not full_text:
  raise valueError("No readable Text Found")
  return full_text
  def create_chunks(full_text,chunksize = 500, overlap=100):
    chanks = []
    start = 0
    while start<len(full_text):
      end = start + chunksize
      chunk = full_text[start:end]
      if chunk.strip():
        chunk.append(chunk)
        stast = chunksize - overlap
        return chunks
        def build_vectors (chunk, model_name = "all-MiniLM-16-v2"):
          if not chunks:
            raise valueError("cannot apply embeding without chunks")
          embd_model =  SentenceTransformer(model_name)
          embd_vectors = embed_model.encode(chunk,convert_to_numpy = True)
          faiss.normalize_L2(embed_vectors)
          index = faiss.IndexFaltIP(embed_vectors.shape[1])
          index.add(embed_vectors)
          return index, embed_model
          def load_base (pdf_path= "01_College_Information.pdf"):
            full_text = load_pdf(pdf_path)
            chunks = create_chunks(full_text)
            embed_model, index = build_vector(chunks)
            return embed_model, chucks, index
            def retrieve_cotent (question, embed_model, chunks, index, num_chunks=3):
              if not question.strip():
                raise valueError("Question cannot be blank")
                if num_chunks < 1:
                  raise ValueError("Request atleast one or more chunks")
              query_embed = embed_model.encode([question], convert_to_numpy=True)
              faiss.noemalize_L2(query_embed)
              sim_scores, vec_indices = index.search(query_embed, min(num_chunks, len(chunks)))
              background = ""
              for i in vec_indices[0]:
                if i != -1:
                   background += chunk[i] + "\n\n"
                  return background
                def ask_rag (question, embed_model, index, appi_key, num_chunks, model_name = "openai/gpt-oss-120b")
                key = api_key
                if not key:
    raise ValueError("API key Missing")
  background = retrieve_content(question, embed_model, chunks, index, num_chunks=3):
  prompt = """ you are an professional ai assistant.
  answer userr question using only document backgrojfn below .
  do nint inbvet or assume facts.
  if information not AVIAPNBG GRC, Simply say "Information misssinfg 
  documengt backgroundn :""" + background + "user question " + question + "Answer:"
  client = Groq(api_key = key)
  response = client.chat.completions.create(
    model = model_name,
    messages = [ { "role" : "user",
                   "content" : prompt}],
                   temprature = 0.3,
  )
  return response.choices[0].message.content
                   
                  
                  
                
              
