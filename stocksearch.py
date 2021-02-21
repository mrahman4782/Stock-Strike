from bs4 import BeautifulSoup
import requests, smtplib, time
from flask import Flask, render_template, request, url_for
from threading import Thread

app = Flask(__name__)

@app.route('/')
def progstart():
    return render_template("site.html")

@app.route('/start_task')
def start_task():
    def do_work(stockInput, targetprice, email):
        targetprice = float(targetprice)
        while True:
            
            URL = "https://finance.yahoo.com/quote/" + stockInput.upper() + "?p=" + stockInput.upper() + "&.tsrc=fin-srch"

            htmlFound = requests.get(URL).text

            retrieved = BeautifulSoup(htmlFound, 'html')

            price = retrieved.find("span", class_ = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text

            oldprice = float(price.replace(",", ""))
            newtargetprice = price.replace(",", "")

            print("The price is: " + price)

            newprice =  float(price.replace(",", ""))

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            
            
            
            server.login("email", "password")
            
            head = stockInput + " price update!"
            
            if oldprice < targetprice:

                if newprice >= targetprice:

                    body = stockInput.upper() + " rose to " + str(newprice) + "!"
                    message = f"Subject: {head}\n\n{body}"
                    server.sendmail("sstrikebot@gmail.com", email, message)
                    
            if oldprice > targetprice:

                if newprice <= targetprice:

                    body = stockInput.upper() + " fell to " + str(newprice) + "!"
            
                    message = f"Subject: {head}\n\n{body}"
                    server.sendmail("sstrikebot@gmail.com", email, message)

            if oldprice == targetprice:

                    body = stockInput.upper() + " has reached $" + str(newprice) + "!"
                
                    message = f"Subject: {head}\n\n{body}"
                    server.sendmail("sstrikebot@gmail.com", email, message)
            time.sleep(30)

    kwargs = {
            'stockInput':request.args.get('ticker'),
            'targetprice':request.args.get('target'),
            'email':request.args.get('email')
            }
    print(request.args)
    thread = Thread(target=do_work, kwargs=kwargs)
    thread.start()
    return render_template("site.html")

if __name__ == "__main__":
    app.run(debug=True)
