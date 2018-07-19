# We Got Lunch

We got it.

Our food hero. Zopa Hackathon 2018.

## Run It

To run the app, go to the root directory of this repository and run:

> python -c "from wegotlunch import api; api.app.run();"

## Endpoints

  * **/listItems**

> http://127.0.0.1:5000/listItems

  * **/addItem**
      * placeName
      * itemName
      * price
      * thumbsUpCount
      * thumbsDownCount
      
> http://127.0.0.1:5000/addItem?placeName=dfsfds&itemName=fdsfds&price=4343&thumbsUpCount=330&thumbsDownCount=434

