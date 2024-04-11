from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

database_path = "odrive_data.db"

def get_time_range(trial_id):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("SELECT MIN(time), MAX(time) FROM ODriveData WHERE trial_id = ?", (int(trial_id),))
    time_range = cursor.fetchone()
    print(time_range)
    conn.close()
    return time_range

def get_motor_position_data(trial_id, node_id, time_string):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    # Convert the time_string to a float and round it to match the database precision
    time_value = round(float(time_string), 2)  # Adjust the rounding as per your database precision
    delta = .05 # Adjust delta based on the granularity of your time data

    start_time = time_value - delta
    end_time = time_value + delta

    print(f"Fetching data for Trial ID: {trial_id}, Node ID: {node_id}, Time Range: {start_time} to {end_time}")

    sql_query = """
    SELECT position,
            velocity,
            torque_target,
            torque_estimate,
            bus_voltage,
            bus_current,
            iq_setpoint,
            iq_measured,
            electrical_power,
            mechanical_power, 
            fet_temp, 
            motor_temp
    FROM ODriveData
    WHERE trial_id = ? AND node_id = ? AND time BETWEEN ? AND ?
    """
    cursor.execute(sql_query, (int(trial_id), int(node_id), float(start_time), float(end_time)))
    motor_position_data = cursor.fetchall()
    print(motor_position_data)
    conn.close()

    return [{'position': mp[0],
             'velocity': mp[1],
             'torque_target': mp[2],
             'torque_estimate':mp[3],
             'bus_voltage':mp[4],
             'bus_current':mp[5],
             'iq_setpoint':mp[6],
             'iq_measured':mp[7],
             'electrical_power':mp[8],
             'mechanical_power':mp[9],
             'fet_temp':mp[10],
             'motor_temp':mp[11]
            } for mp in motor_position_data]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON received'}), 400
        if 'node_id' not in data:
            return jsonify({'error': 'No node_id in JSON'}), 400
        
        node_id = data['node_id']
        if not node_id:
            return jsonify({'error': 'Empty node_id'}), 400
        
        motor_data = get_motor_position_data(node_id)  # This should be updated to your correct function call
        return jsonify(motor_data)
    
    return render_template('index.html')

@app.route('/get_position_data', methods=['POST'])
def get_position_data():
    data = request.get_json()
    trial_id = data.get('trial_id')
    node_id = data.get('node_id')
    time = data.get('time')
    motor_position_data = get_motor_position_data(trial_id, node_id, time)
    if motor_position_data:
        return jsonify(motor_position_data)
    else:
        return jsonify([]), 200  # No data found, but the request was handled correctly

@app.route('/get_time_range', methods=['POST'])
def get_time_range_route():
    data = request.get_json()
    trial_id = data.get('trial_id')
    time_range = get_time_range(trial_id)
    return jsonify({'min': time_range[0], 'max': time_range[1]})

if __name__ == '__main__':
    app.run(debug=True)
