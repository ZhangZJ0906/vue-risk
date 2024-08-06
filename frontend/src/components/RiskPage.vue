<template>

    <h1 class="text-center my-5" >RISK</h1>
    <p>&nbsp;</p>
    
    <div class="container">
        <div class="row  justify-content-center my-5">
            <div class="col-12">
                <form action="/backend/api.php" method="post">
                    <input class="in" type="text" id="company" name="company" placeholder="請輸入公司名稱" />
                    <br />
                    <input class="in" type="number" id="Compiled" name="Compiled" placeholder="請輸入公司統編" />
                    <button type="submit" class="btn btn-primary btn-lg submit-btn ">送出</button>
                </form>
                <p>
                    投資乃一場挑戰，充滿著不確定性與變數，無處不在的風險像影子一樣伴隨您。在您追求財務目標之際，請謹慎而深思熟慮地前進，絕對不要掉以輕心。過分自信與尋求高回報的渴望可能成為您前進道路上的魔咒，導致潛在的損失。為了降低風險，請確保您充分了解您的投資目標、風險承受能力和投資時間範圍，以制定適合您的策略。
                    務必多元化您的投資組合，將您的資金分散投入多個資產類別或市場，以減輕單一資產或市場波動所帶來的衝擊。定期監控和重新評估您的投資，以確保它們仍然符合您的長期財務目標。記住，投資不是一場速成致富的競賽，而是一場長期的旅程。
                    在此過程中，謹記選擇明智且審慎的投資，並保持耐心，這將有助於您實現長期財務成功。不要被瞬間的市場波動或短期的風險擾亂您的目標，堅定地秉持著長期視野，這是實現財務穩健和成功的關鍵。
                </p>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "RiskPage",
};
</script>
<style scoped src="../styles/style.css"></style>
