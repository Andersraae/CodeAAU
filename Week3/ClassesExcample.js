class Animal{
    constructor(name, age, nrLegs){
        this.name = name;
        this.age = age;
        this.nrLegs = nrLegs;
    }

    /**
     * 
     * @param {String} name nameOfAnimal
     */
    greet(name){
        console.log("Hello from animal " + this.name);
    }
}

let lion = new Animal('Lion', 36, 3);
lion.greet();
console.log(lion.name);

class Dog extends Animal{
    constructor(name, age, weight, color){
        super(name, age, 4);
        this.weight = weight;
        this.color = color;
    }
}

let dog1 = new Dog('Bernard', 22, 2, 'Bluuuu');
dog1.greet('Dfe');
console.log(dog1.color);
dog1.name = 'Bernard den 3.';
dog1.greet();