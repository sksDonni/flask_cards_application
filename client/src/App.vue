<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="container">
    <header>
      <div class="wrapper">
        <div class="image-logo">
          <img  src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrklIYyvLNcbwNtxSfjOuZyCTibTzrX8UbLBtkiHw0UzGLUF44k5lkNk5LIXS7NtYgT2c&usqp=CAU">
        </div>
        <nav v-if="isAuth() == true">
          <RouterLink to="/">Home</RouterLink>
          <a @click="logout">Logout</a>
        </nav>
        <nav v-else>
          <RouterLink to="/register">Register</RouterLink>
          <RouterLink to="/login">Login</RouterLink>
        </nav>
      </div>
    </header>
    <div class="content-container">
      <h1 class="heading">
        Flask Cards Application
      </h1>
      <RouterView />
    </div>
  </div>
</template>
<script>
export default {
  methods:{
    isAuth(){
      if(localStorage.getItem('auth_token')){
        return true
      }
      return false
    },
    logout(){
      localStorage.clear('auth-token')
      this.$router.push('/login')
    }
  },
  async mounted(){
    console.log(this.$store.state, this.$store.dispatch)
    await this.$store.dispatch('fetchDirectories')
  }
}
</script>

<style>
@import '@/assets/base.css';

#app {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;

  font-weight: normal;
}

header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

a,
.green {
  text-decoration: none;
  color: hsla(160, 100%, 37%, 1);
  transition: 0.4s;
}

@media (hover: hover) {
  a:hover {
    background-color: hsla(160, 100%, 37%, 0.2);
  }
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  body {
    display: flex;
    place-items: center;
  }

  #app {
    display: grid;
    grid-template-columns: 1fr 1fr;
    padding: 0 2rem;
  }

  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
