<template>
    <div>
        <h1> Register </h1>
        <hr />
        <form @submit.prevent @submit="register">
            <div>
                <label>Username</label>
                <input type="text" v-model="values.username" />
            </div>
            <div>
                <label>Firstname</label>
                <input type="text" v-model="values.firstname" />
            </div>
            <div>
                <label>Lastname</label>
                <input type="text" v-model="values.lastname" />
            </div>
            <div>
                <label>Email</label>
                <input type="text" v-model="values.email" />
            </div>
            <div>
                <label>password</label>
                <input type="password" v-model="values.password" />
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
                username:'',
                firstname:'',
                lastname:'',
                email:'',
                password:'',
            },
        }
    },
    methods:{
        register(){
            let data_submitted = this.values
            this.$store.dispatch("registerUser", data_submitted, this.$router)
            .then(response => {
                if(response.status == 200){
                    this.$router.push('/login')
                }
            })
        }
    },
}
</script>
