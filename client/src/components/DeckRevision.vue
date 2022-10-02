<template>
    <div>
        <h1>
            <button @click="rearrange" v-if="started == false" class="main-button">
                Begin
            </button>
        </h1>
        <!-- <button>
            <router-link :to="{name:'add_card', params:{id:deck_id}}">
                Add Cards
            </router-link>
        </button> -->
        <br/>
        <div v-if="main_queue.length !== 0">
                <h1 class="heading">{{ main_queue[0].front }}</h1>
                <div class="control-pannel">
                    <button class="such-button"><router-link :to="{name:'edit_card', params:{id:main_queue[0].id}}">
                        Edit Card
                    </router-link>
                    </button>
                    <button @click="reveal" class="such-button">
                        Show Answer
                    </button>
                    <button @click="delete_card(main_queue[0].id)" class="such-button">
                        Delete Card
                    </button>
                </div>
                <div v-if="reveal_bool == true">
                    <h1 class="heading">{{ main_queue[0].back }}</h1>
                    <div class="control-pannel-2">
                        <button @click="easy_click" class="main-button">
                            Easy
                        </button>
                        <button @click="medium_click" class="main-button">
                            Medium
                        </button>
                        <button @click="hard_click" class="main-button">
                            Hard
                        </button>
                        <button @click="finish" class="main-button">
                            Finish
                        </button>
                    </div>
                </div>  
        </div>
        <div v-else-if="main_queue.length==0 && easy_queue.length==0 && medium_queue.length == 0">
            <h2 class="heading">No Cards in this Deck</h2>
        </div>
        <div v-else>
            <h2 class="heading">
                You are done for the day
            </h2>
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex'
export default{
    data(){
        return {
            easy_queue: [],
            medium_queue:[],
            hard_queue:[],
            main_queue:[],
            reveal_bool : false,
            started: false
        }
    },
    methods:{
        delete_card(id){
            console.log(id)
            this.$store.dispatch("deleteCardById", {id})
            .then(res => {
                if(res.status == 200){
                    this.main_queue.shift()
                    this.$router.push(`/deck/${deck_id}/revision`)
                }
            })
        }
    },
    computed:{
        ...mapState({
            deck_name: state => state.individualDeck.deck_name,
            deck_cards: state => state.individualDeck.deck_cards,
            deck_id: state => state.individualDeck.deck_id
        }),
        rearrange(){
            if(this.deck_cards)
            {
                this.started = !(this.started)
                this.easy_queue = this.deck_cards.filter(card => card.level>5)
                this.medium_queue = this.deck_cards.filter(card => card.card_level < 6 && card.card_level > -5)
                this.hard_queue = this.deck_cards.filter(card => card.card_level < -5)
                this.main_queue = this.main_queue.concat(this.hard_queue).concat(this.medium_queue).concat(this.easy_queue)
                this.reveal_bool = false
            }
        },
        reveal(){
            this.reveal_bool = !(this.reveal_bool)
        },
        easy_click(){
            let top = this.main_queue.shift()
            console.log(top.card_level)
            if(top.card_level !== 1){
                top.card_level += 1
                this.$store.dispatch("updateCardLevel", top)
                this.main_queue.push(top)
            }
            else{
                top = this.main_queue.pop()
            }
            this.reveal_bool = !(this.reveal_bool)
        },
        medium_click(){
            let top = this.main_queue.shift()
            if(top.card_level == -1){
                top.card_level = 0
                this.$store.dispatch("updateCardLevel", top)
            }else{
                top.card_level -= 1
                this.$store.dispatch("updateCardLevel", top)
            }
            this.main_queue.push(top)
            this.reveal_bool = !(this.reveal_bool)
        },
        hard_click(){
            let top = this.main_queue.shift()
            if(top.card_level !== -1){
                top.card_level = -1
                this.$store.dispatch("updateCardLevel", top)
            }
            this.main_queue.push(top)
            this.reveal_bool = !(this.reveal_bool)
        },
        finish(){
            let score = 0
            for(let i=0; i<this.main_queue.length; i++)
            {
                score += this.main_queue[i].card_level
            }
            console.log(this.$store.state.individualDeck)
            let updated_deck_level = {...this.$store.state.individualDeck, dir_level:score}
            console.log(updated_deck_level)
            this.$store.dispatch("updateDirectoryLevel", updated_deck_level)
            .then(response => {
                if(response.status == 200){
                    this.$router.push(`/deck/${res.deck_id}`)
                }
            })
            
        },
    },
    mounted(){
        let id = this.$route.params.id
        console.log(id)
        this.$store.dispatch("fetchDeckById", {id})
    }
}
</script>
