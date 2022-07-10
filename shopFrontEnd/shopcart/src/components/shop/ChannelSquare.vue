<template>
<!-- 频道广场 -->
  <div id="channel-square">
    <img src="@/assets/backImage/channel-square.png" alt="" />
    <ul>
      <li>
        <div class="title">
          <h2>优购国际</h2>
          <span>快享全球好货</span>
        </div>
        <div class="image">
          <router-link :to='{name: "Search", query:{search:"冰箱",rule:1,price:0,sales:0,index:1}}'>
            <img src="@/assets/channel/one.jpeg" alt="" />
          </router-link>
          <router-link :to='{name: "Search", query:{search:"冰箱",rule:1,price:0,sales:0,index:1}}'>
            <img src="@/assets/channel/two.jpeg" alt="" />
          </router-link>
        </div>
      </li>
      <li>
        <div class="title">
          <h2>生活家电</h2>
          <span>潮流小家电</span>
        </div>
        <div class="image">
          <router-link :to='{name: "Search", query:{search:"手机",rule:1,price:0,sales:0,index:1}}'>
            <img src="@/assets/channel/three.jpeg" alt="" />
          </router-link>
          <router-link :to='{name: "Search", query:{search:"手机",rule:1,price:0,sales:0,index:1}}'>
            <img src="@/assets/channel/four.png" alt="" />
          </router-link>

        </div>
      </li>
      <li>
        <div class="title">
          <h2>服饰家纺</h2>
          <span>品质服饰</span>
        </div>
        <div class="image">
          <router-link :to='{name: "Search", query:{search:"电视",rule:1,price:0,sales:0,index:1}}'>
            <img src="@/assets/channel/five.jpeg" alt="" />
          </router-link>
          <router-link :to='{name: "Search", query:{search:"家纺",rule:1,price:0,sales:0,index:1}}'>
            <img src="@/assets/channel/six.jpeg" alt="" />
          </router-link>
        </div>
      </li>
      <li>
        <div class="title">
          <h2>冰箱洗衣机</h2>
          <span>正品行货</span>
        </div>
        <div class="image">
          <router-link :to='{name: "Search", query:{search:"空调",rule:1,price:0,sales:0,index:1}}'>
            <img src="@/assets/channel/seven.png" alt="" />
          </router-link>
          <router-link :to='{name: "Search", query:{search:"洗衣机",rule:1,price:0,sales:0,index:1}}'>
            <img src="@/assets/channel/eight.jpeg" alt="" />
          </router-link>
        </div>
      </li>
      <li>
        <div class="title">
          <h2>电视家影</h2>
          <span>家庭影院</span>
        </div>
        <div class="image">
          <router-link :to='{name: "Search", query:{search:"洗发液",rule:1,price:0,sales:0,index:1}}'>
            <img src="@/assets/channel/nine.png" alt="" />
          </router-link>
          <router-link :to='{name: "Search", query:{search:"饮料",rule:1,price:0,sales:0,index:1}}'>
            <img src="@/assets/channel/ten.jpeg" alt="" />
          </router-link>
        </div>
      </li>
      <li>
        <div class="title">
          <h2>优购超市</h2>
          <span>为你挑好的</span>
        </div>
        <div class="image">
          <router-link :to='{name: "Search", query:{search:"奶粉",rule:1,price:0,sales:0,index:1}}'>
            <img src="@/assets/channel/eleven.jpeg" alt="" />
          </router-link>
          <router-link :to='{name: "Search", query:{search:"纸巾",rule:1,price:0,sales:0,index:1}}'>
            <img src="@/assets/channel/tweleve.jpeg" alt="" />
          </router-link>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'channelSquare'
}
</script>

<style scoped lang="less">
#channel-square {
  width: 1155px;
  margin: 15px auto 0;
  img {
    width: 1155px;
  }
  ul {
    width: 1155px;
    height: 510px;
    margin: 0;
    padding: 0;
    display: flex;
    flex-wrap: wrap;
    li {
      width: 378px;
      height: 245px;
      justify-content: space-between;
      border-radius: 15px;
      background-color: white;
      cursor: pointer;
    }
    .title {
      display: flex;
      width: 100%;
      height: 60px;
      h2 {
        font-size: 26px;
        color: #333;
        font-weight: bold;
        margin: 11px 12px 0 16px;
        height: 37px;
        line-height: 37px;
      }
      span {
        font-size: 16px;
        color: #666;
        margin-top: 20px;
        width: 96px;
        height: 22px;
        line-height: 22px;
      }
    }
    .image {
      img {
        width: 165px;
        height: 165px;
        margin: 0 10px;
        &:hover {
          opacity: .8;
        }
      }
    }
    li:nth-child(2) {
      margin: 0 10px;
    }
    li:nth-child(5) {
      margin: 0 10px;
    }
  }
}
</style>
