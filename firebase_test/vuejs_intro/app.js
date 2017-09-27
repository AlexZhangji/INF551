new Vue({
  el:'#vue-app',
  data:{
    name:'Test',
    website:'https://google.com'
  },
  methods:{
    greet:function(time){

      return 'Good ' + time + ' ' +this.name;
    }
  }
});
