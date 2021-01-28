    var preview1 = document.querySelector("#img1");
    var inpfile1    = document.querySelector("#inpFile1");
    var reader  = new FileReader();

    inpfile1.addEventListener("change",function()
    {
      const file=this.files[0];

      if(file){
        const reader=new FileReader();

        reader.addEventListener("load",function(){
          preview1.setAttribute("src", this.result);
        });
      
        reader.readAsDataURL(file);
      }
      else{
        preview1.setAttribute("src","");
      }
    });
    
    var preview2 = document.querySelector("#img2");
    var inpfile2    = document.querySelector("#inpFile2");
    var reader  = new FileReader();

    inpfile2.addEventListener("change",function()
    {
      const file=this.files[0];

      if(file){
        const reader=new FileReader();

        reader.addEventListener("load",function(){
          preview2.setAttribute("src", this.result);
        });
      
        reader.readAsDataURL(file);
      }
      else{
        preview2.setAttribute("src","");
      }
    });
    