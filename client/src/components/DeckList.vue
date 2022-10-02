<template>
  <div>
    <h1>
        {{ dir_name }} Directory
    </h1>
      <!-- <button class="main-button"><router-link :to="{name:'add_deck', params:{id: deck.dir_id}}">
        Add Decks
      </router-link></button> -->

    <div class="dir-wrapper">
      <div v-for="deck in dir_decks" :key="deck.deck_id" class="directories">
        <img src="https://h5p.org/sites/default/files/styles/medium-logo/public/logos/flashcards-png-icon.png?itok=R8D0VXup">
        <h2>
          <router-link :to="{name:'deck', params:{id: deck.deck_id}}">
            {{ deck.deck_name }}
          </router-link>
        </h2>
        <h4>
          Proficiency of this deck : {{ deck.dir_level }}
        </h4>
        <button class="such-button">
          <router-link :to="{name: 'edit_deck', params:{id:deck.deck_id}}">
             Edit Directory
          </router-link>
        </button>
        <button class="such-button" @click="delete_deck(deck.deck_id)">Delete</button>
      </div>
    </div>
    <div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import {useRoute} from "vue-router"
export default {
  setup(){
   const route = useRoute();
  },
  data(){
    return{
      url:{id:this.$route.params.id+"/add_deck"}
    }
  },
  methods:{
    delete_deck(id){
      console.log(id)
      this.$store.dispatch("deleteDeckById", {id})
      .then(res => {
        if(res.status == 200){
          this.$router.push(`/directory/${this.dir_id}`)
        }
      })
    }
  },
  computed:{
    ...mapState({
      dir_name: state => state.individualDir.dir_name,
      dir_decks: state => state.individualDir.dir_decks,
      dir_id: state => state.individualDir.dir_id
    })
  },
  async mounted(){
    this.id = this.$route.params.id
    let aid = this.id
    console.log(this.$route.params)
    this.$store.dispatch("fetchDirectoryById", {id:aid})
  }
}
</script>


