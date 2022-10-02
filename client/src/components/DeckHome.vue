<template>
    <div>
        <div v-if="deck_name !== undefined">
            <h1> {{ deck_name }} Deck</h1>

            <h2>
                Start Revising {{ deck_name }} Deck
            </h2>
            <button class="main-button">
                <router-link :to="{name:'deck_revision', params:id}">
                    Start
                </router-link>
            </button>
        </div>
        <div v-else>
            Loading
        </div>
    </div>
</template>


<script>
import { mapState } from 'vuex'
export default {
    data() {

    },
    computed:{
        ...mapState({
            deck_cards: state => state.individualDeck.deck_cards,
            deck_name: state => state.individualDeck.deck_name,
            deck_id: state => state.individualDeck.deck_id
        })
    },
    async mounted(){
        let id = this.$route.params.id
        console.log(id)
        this.$store.dispatch("fetchDeckById", {id})
    }
}
</script>
