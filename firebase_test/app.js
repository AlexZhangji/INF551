(function() {
    console.log('js file loaded');
    // Joy's apiKey
    // const config = {
    //     apiKey: "AIzaSyDLFK8TCZ14wnZhRNhfyFswMda21yIowf0",
    //     authDomain: "inf551-db90c.firebaseapp.com",
    //     databaseURL: "https://inf551-db90c.firebaseio.com",
    //     projectId: "inf551-db90c",
    //     storageBucket: "inf551-db90c.appspot.com",
    //     messagingSenderId: "562245129922"
    // };

    const config = {
        apiKey: "AIzaSyC0kBKQC-Dgw_FJD9CKfwHtqVQoBG6ePwE",
        authDomain: "test-ji-5fef4.firebaseapp.com",
        databaseURL: "https://test-ji-5fef4.firebaseio.com",
        projectId: "test-ji-5fef4",
        storageBucket: "",
        messagingSenderId: "919809776211"
    };

    firebase.initializeApp(config);

    /*      var big = document.getElementById('big');
          var dbRef = firebase.database().ref().child('text');
          dbRef.on('value', snap => big.innerText = snap.val());*/
    const inputEmail = document.getElementById("inputEmail");
    const inputPassword = document.getElementById("inputPassword");
    const btnIn = document.getElementById("btnIn");
    const btnUp = document.getElementById("btnUp");
    // const btnOut = dp

    btnIn.addEventListener('click', e => {
        // get emails and password
        const email = inputEmail.value;
        const pass = inputPassword.value;
        const auth = firebase.auth();

        firebase.auth().signInWithEmailAndPassword(email, password).catch(function(error) {
            // Handle Errors here.
            var errorCode = error.code;
            var errorMessage = error.message;
            // [START_EXCLUDE]
            if (errorCode === 'auth/wrong-password') {
                alert('Wrong password.');
            } else {
                alert(errorMessage);
            }
            console.log(error);
            // document.getElementById('quickstart-sign-in').disabled = false;
            // [END_EXCLUDE]
        });
    });

    btnUp.addEventListener('click', e => {
        // get emails and password
        const email = inputEmail.value;
        const pass = inputPassword.value;
        const auth = firebase.auth();

        firebase.auth().createUserWithEmailAndPassword(email, password).catch(function(error) {
            // Handle Errors here.
            var errorCode = error.code;
            var errorMessage = error.message;
            // [START_EXCLUDE]
            if (errorCode == 'auth/weak-password') {
                alert('The password is too weak.');
            } else {
                alert(errorMessage);
            }
            console.log(error);
            // [END_EXCLUDE]
        });

    });

    // add realtime listener
    firebase.auth().onAuthStateChanged(
        firebaseUser => {
            if (firebaseUser) {
                console.log(firebaseUser);
            } else {
                console.log('not logged in');
            }
        });
});
