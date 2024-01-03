Products : 
  data : 
    - name 
    - flag (new,sale,feature)
    - price 
    - image 
    - reviews :
      - name 
      - image
      - review 
      - rate 
      - date 
  
    - reviews count 
    - brand :
      - image
      - name 
      - item count 

    - sku
    - images 
    - subtitle 
    - tags 
    - description 


  function:
    - list 
    - detail 
    - brand list 
    - brand detail 
    - search 
    - filter 
    - add to cart 
    - add to wishlist 


Users : 
    - data :
      - username 
      - email 
      - image
      - contact numbers :
        - type (primary , secondary)
        - number 
      - address:
        - type : (home,office,bussines,academy,other)
        - address 



    - functions :
      - auth
      - dashboard 
      - profile 
      - edit profile 
  ----------------------------------
App Orders : 
  - address 
  - product 
  - brand 
  - price 
  - quantity 
  - order_time
  - delivery_time
  - order_id
  - total_item
  - discount 
  - delivery fee
  - status = [Recieved,'Processed','Shipped','Delivered']
