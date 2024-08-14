import {createRouter, createWebHistory} from 'vue-router'
import RiskPage from '../components/RiskPage.vue'
import testPage from '../components/testPage.vue'
import loadingPage from '../components/loadingPage.vue'
import RiskResultPage from '../components/RiskResultPage.vue'

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
    },
    {
        path: '/loading',
        name: 'loadingPage',
        component: loadingPage
    },
    {
        path: '/RiskResult',
        name: 'RiskResultPage',
        component: RiskResultPage
    }
]
const router = createRouter({
    history: createWebHistory(),
    routes
})
export default router