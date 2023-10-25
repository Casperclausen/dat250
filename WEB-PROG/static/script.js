
document.addEventListener("DOMContentLoaded", () => {
  const searchbox = document.getElementById("search-item");
  searchbox.addEventListener("keyup", search);

  let cartIcon = document.querySelector("#shopping-cart-icon");
  let cart = document.querySelector(".shopping-cart");
  let closeCart = document.querySelector("#close-shopping-cart");
  let removeCartButtons = document.getElementsByClassName("cart-remove");
  let quantityInputs = document.getElementsByClassName("cart-quantity");
  let addCartButtons = document.getElementsByClassName("add-cart");
  let buyButton = document.querySelector(".checkout-button");

  function toggleCart() {
    cart.classList.toggle("shopping-cart-active");
  }

  function ready() {
    for (let button of removeCartButtons) {
      button.addEventListener("click", removeCartItem);
    }
  }

  function updateQuantityInputs() {
    for (let input of quantityInputs) {
      input.addEventListener("change", quantityChanged);
    }
  }

  function updateAddCartButtons() {
    for (let button of addCartButtons) {
      button.addEventListener("click", addCartClicked);
    }
  }

  function removeCartItem(event) {
    let buttonClicked = event.target;
    buttonClicked.parentElement.remove();
    updateTotal();
  }

  function quantityChanged(event) {
    let input = event.target;
    if (isNaN(input.value) || input.value <= 0) {
      input.value = 1;
    }
    updateTotal();
  }

  function addCartClicked(event) {
    let button = event.target;
    let shopProducts = button.parentElement;
    let title = shopProducts.querySelector(".product-title").innerText;
    let price = shopProducts.querySelector(".price").innerText;
    let productImage = shopProducts.querySelector("#product-image").src;
    addProductToCart(title, price, productImage);
    updateTotal();
  }

  function addProductToCart(title, price, productImage) {
    let cartShopBox = document.createElement("div");
    cartShopBox.classList.add("cart-box");
    let cartItems = document.querySelector(".cart-content");
    let cartItemsNames = cartItems.querySelectorAll(".cart-product-title");
    for (let i = 0; i < cartItemsNames.length; i++) {
      if (cartItemsNames[i].innerText === title) {
        alert("You have already added this item to cart");
        return;
      }
    }

    let cartBoxContent = `
        <img src="${productImage}" class="cart-image">
        <div class="detail-box">
            <div class="cart-product-title">${title}</div>
            <div class="cart-price">${price}</div>
            <input type="number" value="1" class="cart-quantity">
        </div>
        <i class="fa-solid fa-trash cart-remove"></i>`;
    cartShopBox.innerHTML = cartBoxContent;
    cartItems.appendChild(cartShopBox);
    cartShopBox.querySelector(".cart-remove").addEventListener("click", removeCartItem);
    cartShopBox.querySelector(".cart-quantity").addEventListener("change", quantityChanged);
    ready();
  }

  function thankAndClearCart() {
    alert("Thank you for your purchase!");
    let cartItems = document.querySelector('.cart-content');
    while (cartItems.hasChildNodes()) {
      cartItems.removeChild(cartItems.firstChild);
    }
    updateTotal();
  }

  function updateTotal() {
    let cartContent = document.querySelector(".cart-content");
    let cartBoxes = cartContent.querySelectorAll(".cart-box");
    let total = 0;
    for (let i = 0; i < cartBoxes.length; i++) {
      let cartBox = cartBoxes[i];
      let priceElement = cartBox.querySelector(".cart-price");
      let quantityElement = cartBox.querySelector(".cart-quantity");
      let price = parseFloat(priceElement.innerText.replace("$", ""));
      let quantity = quantityElement.valueAsNumber;
      total += price * quantity;
    }
    total = Math.round(total * 100) / 100;
    document.querySelector(".total-price").innerText = "$" + total;
  }

  cartIcon.addEventListener("click", toggleCart);
  closeCart.addEventListener("click", toggleCart);
  buyButton.addEventListener("click", thankAndClearCart);
  ready();
  updateQuantityInputs();
  updateAddCartButtons();
});


function search() {
  const searchbox = document.getElementById("search-item").value.toUpperCase();
  const storeitems = document.getElementById("product-container");
  const product = storeitems.querySelectorAll(".product");
  
  for (var i = 0; i < product.length; i++) {
      let match = product[i].querySelector(".product-title");

      if (match) {
          let textvalue = match.textContent || match.innerHTML;
          if (textvalue.toUpperCase().indexOf(searchbox) > - 1) {
              product[i].style.display = "";
          } else {
              product[i].style.display = "none";
          }
      }
  }
}

function loginAccount() {
  let username = document.getElementById("username").value;
  let password = document.getElementById("password").value;
  fetch("/login", {
    method:"POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({username:username, password:password}),
  }).then(response => {
    if (response.ok) {
      window.location.href = '/';
    } else {
      response.json().then(data => {
        showErrorModal(data.error);
      });
    }
  });
}

function showErrorModal(error) {
  document.getElementById('errorText').innerText = error;
  var errorModal = new bootstrap.Modal(document.getElementById('errorModal'));
  errorModal.show();
}
