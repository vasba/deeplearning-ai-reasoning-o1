TOOLS = [
   {
      "function":{
         "name":"getVehicleByVIN",
         "description":"Returns the vehicle details including car model for a given vehicle identification number (VIN)",
         "parameters":{
            "type":"object",
            "properties":{
               "arg0":{
                  "type":"string",
                  "description":"A VIN is composed of exactly 17 characters (digits and letters)"
               }
            },
            "required":[
               "arg0"
            ]
         }
      },
      "type":"function"
   },
   {
      "function":{
         "name":"getVehiclesByRegistrationNumber",
         "description":"Returns only VIN, car model, projectCode, modelYear, manufacturedWeek and displayName for a given vehicle registration number.",
         "parameters":{
            "type":"object",
            "properties":{
               "arg0":{
                  "type":"string",
                  "description":"vehicle registration number"
               }
            },
            "required":[
               "arg0"
            ]
         }
      },
      "type":"function"
   },
   {
      "function":{
         "name":"EnglishKnowledgeSearch",
         "description":"""
           The knowledge search tool leverages the user's input translated to English, stripped of stop words, and its English translation to retrieve relevant knowledge articles from an API.
           This is achieved by identifying key information such as vehicle identifiers (VIN, registration number, license plate number) or utilizing the user’s search term when specific identifiers are not available.
           If the user input is lengthy or complex, the tool reformulates it into one or several comprehensive questions that maintain essential details while ensuring clarity, as if asking a human for assistance.
           """,
         "parameters":{
            "type":"object",
            "properties":{
               "arg0":{
                  "type":"string",
                  "description":"""
                Argument 0 is the English translation of user’s input, WITH STOP WORDS REMOVED, without alterations. If the user input is already in English, this argument will be identical to the user's input with stop words removed.
                If the input is lengthy, the tool may convert it into one or several succinct questions that capture the main points and intent,
                ensuring that the essence of the user's request is preserved without causing information overload.
            """
               },
               "arg1":{
                  "type":"string",
                  "description":"Argument 1 is the English translation of Argument 0, searchTerm, with stop words removed.This argument is provided when the searchTerm is not in English, allowing for retrieval of relevant knowledge articles in English based on the user's original input."
               },
               "arg2":{
                  "type":"string",
                  "description":"argument 2 is optional. It must be a valid Vehicle Identification Number (VIN), consisting of exactly 17 characters (digits and letters only) and conform with regex [A-HJ-NPR-Z0-9]{17}."
               },
               "arg3":{
                  "type":"string",
                  "description":"argument 3 is optional. It is the vehicle's registration number also known as license plate number.A registration number looks like this: ABC123 or TE44 ANT or B453TEX."
               }
            },
            "required":[
               "arg0",
               "arg1"
            ]
         }
      },
      "type":"function"
   }
]