from flask import Flask

app = Flask(__name__)

Classes = [
  {
    "Class": "M4",
    "Students": [
      {"name": "Sok Cheapanha", "gender": "Male"},
      {"name": "Seng Veha", "gender": "Male"},
      {"name": "Sophea Oudom", "gender": "Male"},
      {"name": "Som Sodana", "gender": "Female"},
      {"name": "Sothea Monineath", "gender": "Female"},
      {"name": "Song Mengly", "gender": "Male"},
      {"name": "Song Meysorng", "gender": "Female"},
      {"name": "Son Khiev", "gender": "Male"},
      {"name": "Sun Seangheang", "gender": "Male"},
      {"name": "San This Sak Khakna", "gender": "Male"},
      {"name": "Sim Senchamrong", "gender": "Male"},
      {"name": "Samnang Limhor", "gender": "Male"},
      
    ]
  }
]

@app.get("/classes")
def classes():
  return {"classes":Classes}

@app.post("/classes")
def createnew():
  new_class = {
    "class": "M3",
    "Students": [
      {"name": "Leng Henglong", "gender": "Male"},
      {"name": "Chanda", "gender": "Female"},
      {"name": "Vicheka", "gender": "Male"},
      {"name": "Soeurm Ravit", "gender": "Male"},
      {"name": "Sarath Vechyeny", "gender": "Female"},
      {"name": "Sea Mengsrun", "gender": "Male"},
      {"name": "Srun Chhaylin", "gender": "Male"},
      {"name": "Sang Sopheak", "gender": "Female"},
      {"name": "Sou Many", "gender": "Female"},
      {"name": "Phearum Sivmeng", "gender": "Male"},
      {"name": "Oeun Chhenghav", "gender": "Female"}
    ]
  }
  Classes.append(new_class)
  return {"msg": "Congradulations!!"}

if __name__ == '__main__':
  app.run(debug=True)