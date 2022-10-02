<template>
    <div>
        <h1> Edit Card </h1>
        <hr />
        <button @click="populate">
            populate
        </button>
        <form @submit.prevent @submit="edit_card"
        >
            <div>
                <label>Front</label>
                <input type="text" v-model="values.front" />
            </div>
            <div>
                <label>Back</label>
                <input type="text" v-model="values.back" />
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
                front:this.front_data,
                back:this.back_data,
            },
        }
    },
    methods:{
        edit_card(){
            let dir_id = this.dir_id
            let deck_id = this.deck_id
            let id = this.id
            let card_level = this.card_level
            console.log(dir_id, deck_id)
            let data_submitted = { ...this.values, dir_id , deck_id, id, card_level}
            console.log(data_submitted)
            this.$store.dispatch("editCardById", data_submitted)
            .then(response => {
                if(response.status == 200){
                    this.$router.push(`/deck/${deck_id}`)
                }
            })
        },
        populate(){
            this.values.front = this.front_data
            this.values.back = this.back_data
        }
    },
    computed:{
        ...mapState({
            data: state => state.individualCard.dir_id,
            deck_id: state => state.individualCard.deck_id,
            dir_id: state => state.individualCard.dir_id,
            front_data: state => state.individualCard.front,
            back_data: state => state.individualCard.back,
            id: state => state.individualCard.id,
            card_level: state => state.individualCard.card_level
        }),
    },
    mounted(){
        let id = this.$route.params.id
        this.$store.dispatch("fetchCardById", {id})
    }
}
</script>
