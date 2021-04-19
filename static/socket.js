// (esversion: 6)

var socket = io();

socket.on('connect', function() {
    console.log( "Connected..." );
} );

socket.on( 'disconnect', function() {
    console.log( "Disconnected..." );
} );

socket.on("add-vote", function( data ) {
    // console.log("duck")
    if ( data.id != 0 ) {
        console.log(data);
        $(`#aspirant-${data.id}-votes`).html( data.votes );
    }   
})


// delete aspirant
function slotter_gang(id) {
    $.ajax({
        url: `aspirants?id=${id}`,
        type: 'DELETE',
        success: function(data) {
            // alert("dede", data)
            // console.log( `aspirant-${id}` )
            $( `#aspirant-${id}` ).remove();
        }
    })
    // change to ajax call
}