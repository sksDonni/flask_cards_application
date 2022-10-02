<template>
    <div>
        <h1> Edit Deck </h1>
        <hr />
        <button @click="populate">populate</button>
        <form @submit.prevent @submit="edit_deck">
            <div>
                <label>Name</label>
                <input type="text" v-model="values.deck_name" />
            </div>
            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<script>
import { mapState } from 'vuex'
export default{
    data(){
        return{
            values:{
                deck_name:'',
            },
        }
    },
    methods:{
        edit_deck(){
            let dir_id = this.dir_id
            let deck_id = this.deck_id
            let dir_level = this.dir_level
            let data_submitted = { ...this.values, dir_id, deck_id, dir_level}
            console.log(data_submitted)
            this.$store.dispatch("editDeckById", data_submitted)
            .then(res => {
                if(res.status == 200){
                    this.$router.push(`/directory/${dir_id}`)
                }
            })
        },
        populate(){
            this.values.deck_name = this.deck_name
        }
    },
    computed:{
        ...mapState({
            dir_id: state => state.individualDeck.dir_id,
            deck_id: state => state.individualDeck.deck_id,
            dir_level: state => state.individualDeck.dir_level,
            deck_name: state => state.individualDeck.deck_name
        }),
    },
    mounted(){
        let id = this.$route.params.id
        this.$store.dispatch("fetchDeckById", {id})
    }
}
</script>
