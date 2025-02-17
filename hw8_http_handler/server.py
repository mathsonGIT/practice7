import json
from flask import Flask, request
from logger_helper import get_logger
from app import calc


app = Flask(__name__)

server_msgs = []

@app.route('/log', methods=['POST'])
def log():
    """
    Записываем полученные логи которые пришли к нам на сервер
    return: текстовое сообщение об успешной записи, статус код успешной работы

    """
    form = request.form
    print(form)
    server_msgs.append(f"{form['levelname']} | {form['name']} | {form['msg']}")
    return "OK", 200


@app.route('/logs', methods=['GET'])
def logs():
    """
    Рендерим список полученных логов
    return: список логов обернутый в тег HTML <pre></pre>
    """
    return(f'<pre>{server_msgs}</pre>')

# TODO запустить сервер
if __name__ == '__main__':
    #calculator_logger = get_logger('calculator_logger')
    #utils_logger = get_logger('utils_logger')
    #printout()
    #with open('logging_tree.txt' , 'w') as tree_file:
    #    tree_file.write(format.build_description())
    #calculator_logger.info('Привет')
    #utils_logger.info('hello')
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
    #calc('5**3')