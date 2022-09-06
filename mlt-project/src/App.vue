<template>
    <div class="wrapper">
        <!--HEADER-->
        <!--   <iframe width="100%" height="80px" frameborder="0" style="position:sticky; top:0; left:0; z-index:5000" src="../PublicFiles/index_Header.html"></iframe> -->
        <!--END OF HEADER-->
        <!--Promo-->
        <!--   <iframe width="100%" height="150px" frameborder="0" style="position:absolute; top:90px; left:0" src="../PublicFiles/index_PromoHorizontalScroll.html"></iframe>-->
        <!--END OF PROMO-->
        <!-- MAIN CONTAINER -->
        <section class="main-container">
            <h1 id="tools">SciPy</h1>
            <div class="box">
                <a href=""><img src="https://images.unsplash.com/photo-1662375716007-3d61760d6977?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" alt=""></a>
                <a href=""><img src="https://images.unsplash.com/photo-1662375716007-3d61760d6977?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" alt=""></a>
                <a href=""><img src="https://images.unsplash.com/photo-1662375716007-3d61760d6977?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" alt=""></a>
            </div>

            <!--<div class="location" id="home">-->
            <h1 id="tools">TensorFlow</h1>
            <div class="box">
                <a href=""><img src="https://images.unsplash.com/photo-1662375716007-3d61760d6977?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" alt=""></a>
                <a href=""><img src="https://images.unsplash.com/photo-1662375716007-3d61760d6977?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" alt=""></a>
                <a href=""><img src="https://images.unsplash.com/photo-1662375716007-3d61760d6977?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" alt=""></a>
                <a href=""><img src="https://images.unsplash.com/photo-1662375716007-3d61760d6977?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" alt=""></a>

            </div>
            <!--</div>-->


            <h1 id="tools">PyTorch</h1>
            <div class="box">
                <a href=""><img src="https://images.unsplash.com/photo-1662375716007-3d61760d6977?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" alt=""></a>
                <a href=""><img src="https://images.unsplash.com/photo-1662375716007-3d61760d6977?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" alt=""></a>

            </div>
        </section>
        <!-- END OF MAIN CONTAINER -->
        <!--FOOTER -->
        <!--    <iframe width="100%" height="300px" frameborder="0" src="../PublicFiles/index_Footer.html"></iframe>-->
        <!--END OF Footer-->

    </div>
</template>

<script>
    export default {
        name: 'App',

    }
</script>

<style>
    /* CSS VARIABLES */
    :root {
        --primary: #141414;
        --light: #F3F3F3;
        --dark: #686868;
    }

    html, body {
        width: 100vw;
        min-height: 100vh;
        margin: 0;
        padding: 0;
        background-color: var(--primary);
        color: var(--light);
        font-family: Arial, Helvetica, sans-serif;
        box-sizing: border-box;
        line-height: 1.4;
    }

    img {
        max-width: 100%;
        border: 4px solid white;
    }

    h1 {
        padding-top: 60px;
    }

    .wrapper {
        margin: 0;
        padding: 0;
    }

    /* MAIN CONTIANER */
    .main-container {
        padding: 50px;
    }

    .box {
        display: grid;
        grid-gap: 20px;
        grid-template-columns: repeat(6, minmax(100px, 1fr));
    }

        .box a {
            transition: transform .3s;
        }

            .box a:hover {
                transition: transform .3s;
                -ms-transform: scale(1.4);
                -webkit-transform: scale(1.4);
                transform: scale(1.4);
            }

        .box img {
            border-radius: 2px;
        }

    /* LINKS */
    .link {
        padding: 50px;
    }

    .sub-links ul {
        list-style: none;
        padding: 0;
        display: grid;
        grid-gap: 20px;
        grid-template-columns: repeat(4, 1fr);
    }

    .sub-links a {
        color: var(--dark);
        text-decoration: none;
    }

        .sub-links a:hover {
            color: var(--dark);
            text-decoration: underline;
        }

    .logos a {
        padding: 10px;
    }

    .logo {
        color: var(--dark);
    }


    /* MEDIA QUERIES */

    @media(max-width: 900px) {

        header {
            display: grid;
            grid-gap: 20px;
            grid-template-columns: repeat(2, 1fr);
            grid-template-areas:
                "nt nt nt  .  .  . sb . . . "
                "mn mn mn mn mn mn  mn mn mn mn";
        }

        .box {
            display: grid;
            grid-gap: 20px;
            grid-template-columns: repeat(4, minmax(100px, 1fr));
        }
    }

    @media(max-width: 700px) {

        header {
            display: grid;
            grid-gap: 20px;
            grid-template-columns: repeat(2, 1fr);
            grid-template-areas:
                "nt nt nt  .  .  . sb . . . "
                "mn mn mn mn mn mn  mn mn mn mn";
        }

        .box {
            display: grid;
            grid-gap: 20px;
            grid-template-columns: repeat(3, minmax(100px, 1fr));
        }

        .sub-links ul {
            display: grid;
            grid-gap: 20px;
            grid-template-columns: repeat(3, 1fr);
        }
    }

    @media(max-width: 500px) {

        .wrapper {
            font-size: 15px;
        }

        header {
            margin: 0;
            padding: 20px 0 0 0;
            position: static;
            display: grid;
            grid-gap: 20px;
            grid-template-columns: repeat(1, 1fr);
            grid-template-areas:
                "nt"
                "mn"
                "sb";
            text-align: center;
        }

        .netflixLogo {
            max-width: 100%;
            margin: auto;
            padding-right: 20px;
        }

        .main-nav {
            display: grid;
            grid-gap: 0px;
            grid-template-columns: repeat(1, 1fr);
            text-align: center;
        }

        h1 {
            text-align: center;
            font-size: 18px;
        }



        .box {
            display: grid;
            grid-gap: 20px;
            grid-template-columns: repeat(1, 1fr);
            text-align: center;
        }

            .box a:hover {
                transition: transform .3s;
                -ms-transform: scale(1);
                -webkit-transform: scale(1);
                transform: scale(1.2);
            }

        .logos {
            display: grid;
            grid-gap: 20px;
            grid-template-columns: repeat(2, 1fr);
            text-align: center;
        }

        .sub-links ul {
            display: grid;
            grid-gap: 20px;
            grid-template-columns: repeat(1, 1fr);
            text-align: center;
            font-size: 15px;
        }
    }
</style>
