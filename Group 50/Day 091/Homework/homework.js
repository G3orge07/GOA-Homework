
const product1 = {
    name : 'iPhone 16',
    price: 799,
    link : 'https://cdn0.it4profit.com/s3size/rt:fill/w:900/h:900/g:no/el:1/f:webp/plain/s3://cms/product/e8/d4/e8d4e563ab4868e7f6ddcd3e35034c1b/250331120205875926.webp',
    quantity: 0
}
const product2 = {
    name : 'iPhone 15',
    price : 699,
    link : 'https://cdn0.it4profit.com/s3size/rt:fill/w:900/h:900/g:no/el:1/f:webp/plain/s3://cms/product/57/4c/574c1f60b8f818205c0c1c40d48b21a7/250331120239557883.webp',
    quantity : 0
}
const product3 = {
    name : 'AirPods 4',
    price : 179,
    link : 'https://s3.zoommer.ge/site/7b281df2-7b42-4453-ba7f-f210a5835fb2_Thumb.jpeg',
    quantity : 0
}
const product4 = {
    name : 'Apple Watch 10',
    price : 399,
    link : 'https://iplus.com.ge/images/detailed/11/Apple_Watch_Series_10_46mm_GPS_Rose_Gold_Aluminum_Sport_Band_Light_Blush_PDP_Image_Position_1__ce-WW.jpg',
    quantity : 0
}
const product5 = {
    name: 'Apple Watch SE',
    price : 249,
    link: 'https://www.apple.com/newsroom/images/product/watch/lifestyle/Apple_watch-se-watchface_09152020_carousel.jpg.large.jpg',
    quantity : 0
}
const product6 = {
    name: 'Apple Vision Pro',
    price : 3499,
    link: 'https://i0.wp.com/www.eseibusinessschool.com/wp-content/uploads/2023/06/Apple-vision-pro.webp?resize=640%2C422&ssl=1',
    quantity : 0
}
const product7 = {
    name: 'MacBook Pro 13"',
    price : 1499,
    link: 'https://alta.ge/images/detailed/253/GEGE_MacBookPro-13-inch-M2_Q322_Space_Gray_PDP-Image-2_7lm4-13.jpg',
    quantity : 0
}
const product8 = {
    name: 'MacBook Pro 14"',
    price : 1799,
    link: 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mbp14-spaceblack-select-202410?wid=904&hei=840&fmt=jpeg&qlt=90&.v=1728916305295',
    quantity : 0
}
const product9 = {
    name: 'MacBook Air 13"',
    price : 999,
    link: 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mba13-skyblue-select-202503?wid=904&hei=840&fmt=jpeg&qlt=90&.v=1741885365897',
    quantity : 0
}
const product10 = {
    name: 'iPad Pro',
    price : 999,
    link: 'https://www.apple.com/v/ipad-pro/as/images/overview/contrast/product-tile/ipad_pro__ea93uc0cnvsm_large_2x.jpg',
    quantity : 0
}
const product11 = {
    name: 'iPad Air',
    price : 599,
    link: 'https://www.apple.com/v/ipad-pro/as/images/overview/contrast/product-tile/ipad_air__crdt2g2u9z0i_large_2x.jpg',
    quantity : 0
}
const product12 = {
    name: 'Apple Pencil',
    price : 79,
    link: 'https://www.apple.com/v/apple-pencil/af/images/overview/usb-c/apple_pencil__bznzcb8von8i_large_2x.jpg',
    quantity : 0
}
const product13 = {
    name: '',
    price : 0,
    link: '',
    quantity : 0
}
const product14 = {
    name: '',
    price : 0,
    link: '',
    quantity : 0
}
const product15 = {
    name: '',
    price : 0,
    link: '',
    quantity : 0
}
const product16 = {
    name: '',
    price : 0,
    link: '',
    quantity : 0
}

let products = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10, product11, product12]

const cartBtn = document.getElementById('cart')
const cartWindow = document.getElementById('cart-window')



const main = document.getElementById('main')


cartBtn.addEventListener('click', function(){
    if (cartWindow.style.display == 'none'){
        cartWindow.style.display = 'block'
    }
    else{
        cartWindow.style.display = 'none'
    }
})




for (let i = 0; i < products.length; i++){
    const product = document.createElement('div')
    product.className = 'product'
    product.id = 'product' + String(i)

    const image = document.createElement('img')
    image.src = products[i].link
    product.appendChild(image)

    const title = document.createElement('h3')
    title.textContent = products[i].name
    product.appendChild(title)

    const price = document.createElement('p')
    price.textContent = '$' + String(products[i].price)
    product.appendChild(price)

    const addToCart = document.createElement('div')
    addToCart.className = 'add'
    addToCart.innerHTML = '<img src="shopping_cart_45dp_FFFFFF_FILL0_wght400_GRAD0_opsz48.png" alt="[-]"> <button class="add-btn" id =' +"btn" + String(i) + '>Add To Cart</button>'
    product.appendChild(addToCart)


    main.appendChild(product)
}

let buttons = document.querySelectorAll('.add-btn')
let cart = []

for (let btn of buttons){
    btn.addEventListener('click', function(){
        let index = Number(btn.id[btn.id.length -1])
        products[index].quantity += 1
        if (!cart.includes(products[index])){
            cart.push(products[index])
        }
        cart_update()
    })
}

let total = 0
const cartItems = document.getElementById('cart-items')

function cart_update() {
    cartItems.innerHTML = ''
    for (let i = 0; i < cart.length; i++){
        const product = document.createElement('div')
        product.className = 'cart-product'

        const image = document.createElement('img')
        image.src = cart[i].link
        image.className = 'product-img'
        product.appendChild(image)

        const details = document.createElement('div')
        details.className = 'product-details'
        details.innerHTML = '<h4>' + cart[i].name + '</h4> <p>' + String(cart[i].price) + '</p>'
        product.appendChild(details)

        const quantityCont = document.createElement('div')
        quantityCont.className = 'quantity'

        const imgPlus = document.createElement('img')
        imgPlus.className = 'plus'
        imgPlus.src = 'add_45dp_FFFFFF_FILL0_wght400_GRAD0_opsz48.png'
        imgPlus.addEventListener('click', function(){
            cart[i].quantity += 1
            cart_update()
        })
        const quantity = document.createElement('p')
        quantity.textContent = String(cart[i].quantity)
        const imgMinus = document.createElement('img')
        imgMinus.addEventListener('click', function(){
            if (cart[i].quantity > 0){
                cart[i].quantity -= 1
                cart_update()
            }
        })
        imgMinus.className = 'minus'
        imgMinus.src = 'remove_45dp_FFFFFF_FILL0_wght400_GRAD0_opsz48.png'
        
        quantityCont.appendChild(imgPlus)
        quantityCont.appendChild(quantity)
        quantityCont.appendChild(imgMinus)

        product.appendChild(quantityCont)

        const imgDelete = document.createElement('img')
        imgDelete.className = 'delete'
        imgDelete.src = 'delete_45dp_FFFFFF_FILL0_wght400_GRAD0_opsz48.png'
        imgDelete.addEventListener('click', function(){
            cart[i].quantity = 0
            cart.splice(cart.indexOf(cart[i]), 1)
            cart_update()
        })
        product.appendChild(imgDelete)

        cartItems.appendChild(product)
    }

    const cartTotalH2 = document.getElementById('cart-total-h2')
    let cartTotal = 0
    for (let item of cart){
        cartTotal += item.price * item.quantity
    }
    cartTotalH2.textContent = 'Total - $' + String(cartTotal)
}