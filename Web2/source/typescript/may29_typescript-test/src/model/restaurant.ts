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