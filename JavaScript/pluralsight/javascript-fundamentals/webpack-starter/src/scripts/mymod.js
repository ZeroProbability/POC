export let app = (() => {
    let sayHello = (name) => {
        console.log(`hello ${name}`);
    };
    return {
        sayHello: sayHello
    };
})();

