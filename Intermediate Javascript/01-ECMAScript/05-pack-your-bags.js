


/*
    Let's practice these nifty new operators by planning an intercontinental vacation! 🗺️

    Define a planVacation() function that returns a string array of destinations we plan to visit. It should accept at least two string arguments:
    destinationOne
    destinationTwo
    Use the rest operator so the planVacation() function can have more arguments passed to it.

    Then, execute the planVacation() function and log the results to the console.

    Where in the world will you plan for next?

    const packGroceries = (...items) => {
    return items;
    }
*/
/*
    const packedGroceries = packGroceries("apples", "bananas", "milk");
    const morePackedGroceries = packGroceries("eggs", "bread");

    console.log(packedGroceries);
    console.log(morePackedGroceries);

    Output:
    [ 'apples', 'bananas', 'milk' ]
    [ 'eggs', 'bread' ]
*/

const planVacation = (destinationOne, DestinationTwo, ...moreDestinations) => {
    return [destinationOne, DestinationTwo, ...moreDestinations];
}

console.log(planVacation("Japan", "Italy", "Brazil", "Canada", "Australia"));