const pig = {
  name: "Porky",
  type: "Pig",
  age: 3,
  makeSound () {
    console.log(pig.name + " is a " + pig.age + " year old " + pig.type + " that goes oink, oink!");
  }
};
const sheep = {
    name: "Dolly",
    type: "Sheep",
    age: 4,
    makeSound () {
      console.log(sheep.name + " is a " + sheep.age + " year old " + sheep.type + " that goes baa, baa!");
    }
};
const dog = {
    name: "Buddy",
    type: "Dog",
    age: 5,
    makeSound () {
      console.log(dog.name + " is a " + dog.age + " year old " + dog.type + " that goes woof, woof!");
    }
};

pig.makeSound();
sheep.makeSound();
dog.makeSound();