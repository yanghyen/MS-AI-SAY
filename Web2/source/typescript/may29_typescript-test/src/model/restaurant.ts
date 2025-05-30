// let data = {
//   name: "seattle coffee",
//   category: "cafe",
//   address: {
//     city: "seattle",
//     detail: "somewhere",
//     zieCode: 213123
//   },
//   menu: [{name:"latte", price:4000, category:"coffee"}, {name:"스초생", price:3000, category:"dessert"}]
// }

export type Restaurant = {
    name:string;
    category:string;
    address:Address;
    menu:Menu[]
}

export type Address = {
    city:string;
    detail:string;
    zipCode:number
}

export type Menu = {
    name:string;
    price:number;
    category:string;
}

export type AddressWithoutZip = Omit<Address, 'zipCode'>
export type RestaurantOnlyCategory = Pick<Restaurant, 'category'>

export type ApiResponse<T> = {
    data:T[],       // data가 api 호출에 따라 타입이 달라지니까
    totlaPage:number,
    page:number
}

export type RestaurantResponse = ApiResponse<Restaurant>
export type MenuResponse = ApiResponse<Menu>