from flask import Flask, request
from  utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>Smart Home Monitoring System</h1></body></html>"

@server.post('/update')
def update_status():
    light_status = request.form.get('light_status')  
    fan_status = request.form.get('fan_status')      
    temperature = request.form.get('temperature')

    query = f"""
    INSERT INTO smart_home
    (light_status, fan_status, temperature)
    VALUES ('{light_status}', '{fan_status}', '{temperature}');
    """

    executeQuery(query=query)

    return "Smart home status updated successfully"

@server.get('/status')
def get_status():
    query = """
    SELECT light_status, fan_status, temperature
    FROM smart_home
    ORDER BY temperature DESC
    LIMIT 1;
    """

    data = executeSelectQuery(query=query)

    if not data:
        return "No data available"

    return f"""
    <html>
        <body>
            <h2>Current Smart Home Status</h2>
            <p><b>Light:</b> {data[0][0]}</p>
            <p><b>Fan:</b> {data[0][1]}</p>
            <p><b>Temperature:</b> {data[0][2]} °C</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)
