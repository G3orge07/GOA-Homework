// შექმენით ქვემოთ მოცემული ობიექტის მსგავსი ობიექტი თქვენს სასურველ მანქანაზე და დაამატეთ ფუნქცია CarFullInfo, რომლის გამოძაღებაზეც გამოიტანს მთლიან ინფორმაციას მანქანაზე(აუცილებლად გამოიყენეთ string formatting)

const carInfo = {
    brand : 'BMW',
    model : '3 Series',
    year : 2024,
    color : 'Black',
    isElectric : false,
    CarFullInfo() {
        if (this.isElectric){
            return this.brand + ' ' + this.model + ', released in ' + this.year + ' is ' + this.color + ' and electric.' 
        }
        else{
            return this.brand + ' ' + this.model + ', released in ' + this.year + ' is ' + this.color + '. Not electric.' 
        }
        
    }
}

console.log(carInfo.CarFullInfo())