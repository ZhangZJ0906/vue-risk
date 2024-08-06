import {createRouter, createWebHistory} from 'vue-router'
import RiskPage from '../components/RiskPage.vue'
import testPage from '../components/testPage.vue'

const routes = [
    {
        path: '/Risk',
        name: 'RiskPage',
        component: RiskPage
    },
    {
        path: '/tesr',
        name: 'testPage',
        component: testPage
    }
]
const router = createRouter({
    history: createWebHistory(),
    routes
})
export default router