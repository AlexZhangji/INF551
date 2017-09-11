function appInit() {
    console.log('js file loaded');

    const config = {
        apiKey: "AIzaSyC0kBKQC-Dgw_FJD9CKfwHtqVQoBG6ePwE",
        authDomain: "test-ji-5fef4.firebaseapp.com",
        databaseURL: "https://test-ji-5fef4.firebaseio.com",
        projectId: "test-ji-5fef4",
        storageBucket: "",
        messagingSenderId: "919809776211"
    };

    firebase.initializeApp(config);

    // add realtime listener
    firebase.auth().onAuthStateChanged(
        firebaseUser => {
            if (firebaseUser) {
                console.log(firebaseUser);
            } else {
                console.log('not logged in');
            }
        });
};

function writeUserData(userId, name, email) {
    firebase.database().ref('users/' + userId).set({
        username: name,
        email: email
    });
}


function updateUserData(userId, email) {
    firebase.database().ref('users/' + userId).update({
        email: email
    });
}


function deleteUserData(userId) {
    console.log(userId + ' is deleted.');
    firebase.database().ref('users/' + userId).remove();
}


function postNewUserData(name, email) {
    firebase.database().ref('users/').set({
        username: name,
        email: email
    });
}



function retriveData() {
    userRef = firebase.database().ref("users");
    userRef.on("value", function(snapshot) {
        snapshot.forEach(function(child) {
            console.log(child.key);
            console.log(child.val());
        });
    });
}

function filterData() {
    queryRef =
        firebase.database().ref("users").orderByChild(
            "username").equalTo("David");
    queryRef.on("value", function(snapshot) {
        snapshot.forEach(function(child) {
            console.log(child.key + ": " + child.val());
        });
    });
}



/*      var big = document.getElementById('big');
      var dbRef = firebase.database().ref().child('text');
      dbRef.on('value', snap => big.innerText = snap.val());*/
