# Yunhyeok Lee 
# Tesla Energy Service Engineering Data Engineer Evaluation
# Deployment URL: https://energeservice.herokuapp.com

#======================================{ all imports }==============================================
from flask import Flask, jsonify, request
from datetime import datetime
import numpy as np
import json

#====================================={ global objects }============================================

app = Flask(__name__)

#================================={ json buffer functions }=========================================

def read_buffer():
    with open('errors.json', 'r') as buffer:
        errors = json.load(buffer)
        buffer.close()
        return errors
    
def write_buffer(errors:list):
    with open('errors.json', 'w') as buffer:
        json.dump(errors, buffer)
        buffer.close()
        
#===================================={ /temp POST route }===========================================

@app.post('/temp')
def temperature():
    body = request.get_json()
    try:
        # extracting data from json body
        data = body['data']
        
        # parsing the data
        data = str(data)
        
        # extracting values from data
        values = data.split(':') 
        if not values or len(values)!=4:
            raise OverflowError()
        
        device_id, epoch_ms, label, temperature = values
        
        # validating different parameters
        label = str(label).replace("'","")
        if label != 'Temperature':
            raise ValueError()
    
        temperature = np.float64(temperature)
        device_id = np.int32(device_id)
        epoch_ms = np.int64(epoch_ms)
        
        # returning response for if temperature is equle or over 90
        if temperature >= 90:
            # generating formated time
            now = datetime.now()
            formatted_time = now.strftime("%Y/%m/%d %H:%M:%S")
            return jsonify({"overtemp": True, "device_id": int(device_id), "formatted_time": formatted_time})
        
        # returning response for if temperature is less then 90
        return jsonify({"overtemp": False})
        
    except KeyError as e:
        # returning error if any field is missing in request body
        return jsonify({'error':f'{e} is required'}), 400
    
    except ValueError as e:
        # adding the data to buffer and returning error
        errors = read_buffer()
        errors.append(data)
        write_buffer(errors)
        return jsonify({'error':'bad request'}), 400
    
    except OverflowError as e:
        # adding the data to buffer and returning error
        errors = read_buffer()
        errors.append(data)
        write_buffer(errors)
        return jsonify({'error':'bad request'}), 400
        
#===================================={ /errors GET route }=========================================

@app.get('/errors')
def get_errors():
    errors = read_buffer()
    return jsonify({ "errors" : errors })

#==================================={ /errors DELETE route }=======================================

@app.delete('/errors')
def delete_errors():
    write_buffer([])
    return jsonify({"msg": "buffered cleared"})

#============================={ testing part for local envirment }=================================

if __name__ == '__main__':
    app.run(debug=True)
    
#========================================{ code ends }=============================================
