<template>
    <div>
        <h1> Add Cards </h1>
        <hr />
        <form @submit.prevent @submit="add_card" class="main-form"
        >
            <div>
                <label>Front</label>
                <input type="text" v-model="values.front" />
            </div>
            <div>
                <label>Back</label>
                <input type="text" v-model="values.back" />
            </div>
            <button class="such-button" type="submit">Create New Card</button>
        </form>
    </div>
</template>

<script>
import { mapState } from 'vuex'
export default{
    data(){
        return{
            values:{
                front:'',
                back:'',
            },
        }
    },
    methods:{
        add_card(){
            let dir_id = this.dir_id
            let deck_id = this.deck_id
            console.log(dir_id, deck_id)
            let data_submitted = { ...this.values, dir_id , deck_id, user_id:1}
            console.log(data_submitted)
            this.$store.dispatch("addCardByDeck", data_submitted)
            .then(response => {
                if(response.status == 200){
                    this.$router.push(`/deck/${deck_id}`)
                }
            })
        }
    },
    computed:{
        ...mapState({
            data: state => state.individualDeck,
            deck_id: state => state.individualDeck.deck_id,
            dir_id: state => state.individualDeck.dir_id,
        }),
    },
    mounted(){
        let id = this.$route.params.id
        this.$store.dispatch("fetchDeckById", {id})
    }
}
</script>
