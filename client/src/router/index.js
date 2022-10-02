import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DeckListComponent from '../components/DeckList.vue'
import DeckHomeComponent from "../components/DeckHome.vue"
import DeckRevisionComponent from "../components/DeckRevision.vue"
import AddCardComponent from "../components/AddCard.vue"
import AddDeckComponent from "../components/AddDeck.vue"
import AddDirComponent from "../components/AddDir.vue"
import RegisterComponent from  "../components/Register.vue"
import LoginComponent from "../components/Login.vue"
import EditCardComponent from "../components/EditCard.vue"
import EditDeckComponent from "../components/EditDeck.vue"
import EditDirComponent from "../components/EditDir.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/directory/:id',
      name: 'directory',
      component: DeckListComponent
    },
    {
      path: '/deck/:id',
      name: 'deck',
      component: DeckHomeComponent
    },
    {
      path: '/deck/:id/revision',
      name: 'deck_revision',
      component: DeckRevisionComponent
    },
    {
      path: '/deck/:id/addcard',
      name: 'add_card',
      component: AddCardComponent
    },
    {
      path: '/directory/:id/add_deck',
      name: 'add_deck',
      component: AddDeckComponent
    },
    {
      path: '/add_directory',
      name: 'add_dir',
      component: AddDirComponent
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterComponent
    },
    {
      path: '/login',
      name: 'login',
      component: LoginComponent
    },
    {
      path: '/card/:id/edit',
      name: 'edit_card',
      component: EditCardComponent
    },
    {
      path: '/deck/:id/edit',
      name: 'edit_deck',
      component: EditDeckComponent
    },
    {
      path: '/dir/:id/edit',
      name: 'edit_dir',
      component: EditDirComponent
    }
  ]
})

router.beforeEach((to, from, next) => {
  if(to.name == 'register' && !(isAuthenticated())){
    next()
  }
  if(to.name == 'login' && (isAuthenticated())){
    next({name: 'home'})
  }
  else if(to.name == 'register' && (isAuthenticated())){
    next({name: 'home'})
  }
  if (to.name !== 'login' && !(isAuthenticated())) {
    next({ name: 'login' });
  } else {
    next();
  }
});


const isAuthenticated = () => {
  if(localStorage.getItem('auth_token')){
    return true
  }
  else{
    return false
  }
}

export default router
