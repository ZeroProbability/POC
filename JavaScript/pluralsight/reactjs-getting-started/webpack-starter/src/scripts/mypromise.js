let p = new Promise(
    function(resolve, reject) {
        setTimeout(reject, 100, 'some value');
    }
)

p.then(
    value => console.log('fulfilled:' + value),
    error => console.log('rejected:' + error)
);

