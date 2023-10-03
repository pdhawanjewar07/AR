from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app


#   ShopifyModels
@app.route('/getShopifyModels/<string:ShopifyModels>')
def getShopifyModels(ShopifyModels):
    return send_from_directory("./",f"assets/ShopifyModels/{ShopifyModels}")

#   ASSETS
@app.route('/getasset/<string:asset>')
def getasset(asset):
    return send_from_directory("./",f"assets/{asset}")


if __name__ == '__main__':
    app.run(debug=True, port=8080)
