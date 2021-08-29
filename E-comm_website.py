"""login page """

<!DOCTYPE html>
<html>
<style>
    /*set border to the form*/

    form {
        border: 3px solid #f1f1f1;
    }
    /*assign full width inputs*/

    input[type=text],
    input[type=password] {
        width: 100%;
        padding: 12px 20px;
        margin: 8px 0;
        display: inline-block;
        border: 1px solid #ccc;
        box-sizing: border-box;
    }
    /*set a style for the buttons*/

    button {
        background-color: #E3FC7D;
        color: black;
        padding: 14px 20px;
        margin: 8px 0;
        border: none;
        cursor: pointer;
        width: 100%;
    }
    /* set a hover effect for the button*/

    button:hover {
        opacity: 0.8;
    }
    /*set extra style for the cancel button*/

    .cancelbtn {
        width: auto;
        padding: 10px 18px;
        background-color: #f44336;
    }
    /*centre the display image inside the container*/

    .imgcontainer {
        text-align: center;
        margin: 24px 0 12px 0;
    }
    /*set image properties*/

    img.avatar {
        width: 10%;
        border-radius: 20%;
    }
    /*set padding to the container*/

    .container {
        padding: 16px;
    }
    /*set the forgot password text*/

    span.psw {
        float: right;
        padding-top: 16px;
    }
    /*set styles for span and cancel button on small screens*/

    @media screen and (max-width: 300px) {
        span.psw {
            display: block;
            float: none;
        }
        .cancelbtn {
            width: 100%;
        }
    }
</style>

<body>

    <h2>Please authenticate yourself</h2>
    <!--Step 1 : Adding HTML-->
    <form action="/action_page.php">
        <div class="imgcontainer">
            <img src=
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsVDHYfVhbk6hqIV8XZeMZkowfoCZ9oF2Eug&usqp=CAU"
                 alt="Avatar" class="avatar">
        </div>

        <div class="container">
            <label><b>Username</b></label>
            <input type="text" placeholder="Enter Username" name="uname" required>

            <label><b>Password</b></label>
            <input type="password" placeholder="Enter Password" name="psw" required>

            <button type="submit">Login</button>
            <input type="checkbox" checked="checked"> Remember me
        </div>

        <div class="container" style="background-color:#f1f1f1">
            <button type="button" class="cancelbtn">Cancel</button>
            <span class="psw">Forgot <a href="#">password?</a></span>
        </div>
    </form>

</body>

</html>

"""product display page"""

<h1>Shopping Cart</h1>

<div class="shopping-cart">

  <div class="column-labels">
    <label class="product-image">Image</label>
    <label class="product-details">Product</label>
    <label class="product-price">Price</label>
    <label class="product-quantity">Quantity</label>
    <label class="product-removal">Remove</label>
    <label class="product-line-price">Total</label>
  </div>

  <div class="product">
    <div class="product-image">
      <img src="https://5.imimg.com/data5/OE/XM/VX/ANDROID-72559702/1590986891401-jpg-500x500.jpg">
    </div>
    <div class="product-details">
      <div class="product-title">Aashirvad aata</div>
      <p class="product-description"> Aashirvaad ensures locking-in the highest nutritional value in the whole wheat flour. The locked-in dietary fibres and natural nutrients help in easy digestion. </p>
    </div>
    <div class="product-price">100.00</div>
    <div class="product-quantity">
      <input type="number" value="2" min="1">
    </div>
    <div class="product-removal">
      <button class="remove-product">
        Remove
      </button>
    </div>
    <div class="product-line-price">25.98</div>
  </div>

  <div class="product">
    <div class="product-image">
      <img src="https://5.imimg.com/data5/IX/OG/MY-7844719/california-almonds-500x500.jpg">
    </div>
    <div class="product-details">
      <div class="product-title">Wonderland California Almonds</div>
      <p class="product-description">Almonds contain lots of healthy fats, fiber, protein, magnesium and vitamin E. The health benefits of these almonds include lower blood sugar levels, reduced blood pressure and lower cholesterol levels.</p>
    </div>
    <div class="product-price">450</div>
    <div class="product-quantity">
      <input type="number" value="1" min="1">
    </div>
    <div class="product-removal">
      <button class="remove-product">
        Remove
      </button>
    </div>
    <div class="product-line-price">450</div>
  </div>

  <div class="totals">
    <div class="totals-item">
      <label>Subtotal</label>
      <div class="totals-value" id="cart-subtotal">550</div>
    </div>
    <div class="totals-item">
      <label>Tax</label>
      <div class="totals-value" id="cart-tax">3.60</div>
    </div>
    <div class="totals-item">
      <label>Shipping</label>
      <div class="totals-value" id="cart-shipping">15.00</div>
    </div>
    <div class="totals-item totals-item-total">
      <label>Grand Total</label>
      <div class="totals-value" id="cart-total">568.60</div>
    </div>
  </div>

      <button class="checkout">Checkout</button>

</div>

"""billing and checkout page"""

