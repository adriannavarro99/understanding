from flask import Flask , app



app = Flask ( __name__)



@app.route( '/',methods=['GET'] )
def hello ():
    return "Hello World!"

@app.route( '/dojo',methods=['GET'] )

def dojo ():
    return "Dojo"


@app.route( '/say/<id>',methods=['GET'] )

def say(id):
    return "Hi " + id




@app.route( '/repeats/<id>/<someword>',methods=['GET'] )
def world (id,someword):
    for i in range (int(id)):
        return(str(someword))



@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"



    return output


    




if __name__ == "__main__":
    app.run(debug=True)

