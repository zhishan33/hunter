// Initialize your app
var myApp = new Framework7({
    //cache: false,//是否打开 Ajax 缓存,因为Framework7使用ajax加载新页面，最好启用Ajax缓存，特别是你的页面内容不经常更新的时候
    //cacheDuration: 10,//Ajax 缓存时间，在缓存有效期内加载页面不会发起新的ajax请求而是直接使用缓存的结果。默认是10分钟
    //cacheIgnore: [],//不希望被缓存的URL，这是一个字符串数组
    //cacheIgnoreGetParameters:false,//缓存是否忽略get参数，如果为 "true"，那么像 "about.html?id=2" 和 "about.html?id=3" 将会和 "about.html" 是一样的缓存。
    //fastClicks:true,//Fast clicks 是一个内置库，当你点击链接或者提交表单的时候，她会移除300毫秒的延迟。如果你有其他的 fast click 库，你可以禁用这个功能
    //fastClicksDelayBetweenClicks:50,//Minimal allowed delay (in ms) between miltiple clicks
    //fastClicksDistanceThreshold:10,//需要阻止tab事件的距离。当 tap/move 的距离超过这个值的时候，不会触发click事件
    //activeState:true,//启用这个设置时，会给当前点击的元素增加一个 'active-state' class
    //activeStateElemets:'a, button, label, span',//应该在这些元素上加 activeState
    //tapHold:false,//设置长安事件
    //tapHoldDelay:750,//设置元素上长按多长时间时，启动长按事件
    //tapHoldPreventClicks:true,//在长按事件之后，点击事件不会被移除When enabled (by default), then click event will not be fired after tap hold event
    //router:true,//如果你有自己的路由实现，你可以禁用默认的路由
    //ajaxLinks:undefined,//指定哪些链接需要用ajax加载，默认情况下（当为undefined时）Framework7 会使用ajax加载所有的链接。你可以通过设置一个CSS选择器来指定需要通过Ajax加载的链接，比如 "a.ajax" - 只有class 为 "ajax" 的链接。
    //dynamicPageUrl:'',//
    //externalLinks:'.external',//不应该被 Framework7 管理的链接的CSS选择器。比如 ".external" 会匹配到这样的链接 <a href="somepage.html" class="external"> (因为它有 "external" 类)
    //animatePages:true,//如果你想禁用页面切换的动画，就把这个值设置为 false。
    //preloadPreviousPage:true,//预加载上一页，为了能让"滑动返回上一页"功能正常工作，这个值应该设置为 true。
    //pushState:false,//如果你开发web app（而不是通过PhoneGap封装的混合应用)，那么这个功能将很有用（浏览器的URL将会看上去像这样 "http://my-webapp.com/#/about.html")。用户可以通过浏览器默认的前进后退按钮来操作。
    //swipeBackPage:false,//开启/关闭滑动返回上一页功能。
    //swipeBackPageThreshold:0,//单位px，当滑动距离超过这个数值的时候，滑动返回上一步功能就会生效
    //swipeBackPageActiveArea:30,//Value in px. Width of invisible left edge of the screen that triggers swipe back action
    //swipeBackPageAnimateShadow:true,//打开/关闭 滑动返回时候的 box-shadow 动画。关闭这个功能可以提高性能。
    //swipeBackPageAnimateOpacity:true,//打开/关闭 滑动返回时候的半透明效果。关闭这个功能可以提高性能。
    //sortable:false,//如果你不使用可排序列表，可以禁用这个功能。因为禁用之后可能会有潜在的性能提升。
    //swipeout:true,//如果你使用滑动删除，禁用这个选项，可能会带来潜在的性能提升。
    //swipeoutNoFollow:false,//滑动删除的时候动画是否跟随手指移动，如果设置为true，那么你滑动的时候动画会自动开始/结束，而不是跟随你手指的位置，这样在老的设备上可能会有更好性能。
    //swipePanel:false,//默认是禁用的，如果你希望通过滑动可以打开 side panel，那么可以设置为 "left" (lef panel) 或者 "right" ( right panel)
    //swipePanelNoFollow:false,//为了兼容老的设备。当设置为 true时，side panel的动画不会跟随你的手指，而是自动开始/结束。
    //panelsCloseByOutside:true,//点击 panel 外面来关闭她。
    //hideNavbarOnPageScroll:false,//设置为true，那么当页面向下滚动的时候，导航栏会自动隐藏；向上滚动的时候会自动出现
    //hideToolbarOnPageScroll:false,//设置为true，那么当页面向下滚动的时候，工具栏会自动隐藏；向上滚动的时候会自动出现。
    //showBarsOnPageScrollEnd:true,//设置为true，那么当页面滚动到底部的时候会自动显示出被隐藏的导航栏和工具栏
    //showBarsOnPageScrollTop:true,////设置为true，那么当页面滚动到底部的时候会自动显示出被隐藏的导航栏和工具栏
    //imagesLazyLoadThreshold:50,//By default images are loaded when they appear on the screen. Use this parameter if you want to load images earlier. Setting it to 50 will load image when it 50 pixels before it appears on viewport
    //imagesLazyLoadSequential:true,//If enabled, then lazy images will be loaded one by one when they appear in viewport
    //imagesLazyLoadPlaceholder:'loading.....',//Lazy load image placeholder source to show while image is not yet loaded. By default it is 1x1 px image
    //template7Pages:true,//设置为true，则会自动使用 Template7 来渲染 ajax或者动态生成的页面。这里有更详细的说明 Template7 Pages
    //template7Data:{},//用来存储Template7 渲染页面所需的数据。这里有更详细的说明：Template7 Pages
    //precompileTemplates:false,//是否自动编译所有的 Template7 模板。这里有更详细的说明：Templates Auto Compilation
    //templates:{},//编译好的 Template7 模板。这里有更详细的说明：Templates Auto Compilation
    //preroute: function (view, options) {
    //    if (!userLoggedIn) {
    //        view.router.loadPage('auth.html'); //load another page with auth form
    //        return false; //required to prevent default router action
    //    }
    //},//这个回调函数可以用来阻止路由器默认的 加载/返回 行为，你可以自己去加载其他页面，重定向，或者做任意你需要的操作。比如我们在用户访问某些页面的时候可以去检查他是否登录，如果未登录就跳转到登录页面
    // preprocess: function (content, url, next) {
    //    if (url === 'people.html') {
    //        // For example, we will retreive template JSON data using Ajax and only after that we will continue page loading process
    //        $$.get('sometemplate.html', function(data) {
    //            // Template
    //            var template = Template7.compile(content);
    //
    //            // Compile content template with received JSON data
    //            var resultContent = template(data);
    //
    //            // Now we call "next" callback function with result content
    //            next(resultContent);
    //        });
    //        // Now we shouldn't return anything
    //    }
    //},//有时候你会在预处理方法中有一些异步的逻辑，比如你用ajax来加载页面。这种情况下，我们提供了 "next" 回调函数，用来传入我们编译或者修改后的内容：

});

// Export selectors engine
var $$ = Dom7;

//// Add view
var mainView = myApp.addView('.view-main', {
    // Because we use fixed-through navbar we can enable dynamic navbar
    dynamicNavbar: true
});// Add view
//
//$$(document).on('pageInit', function (e) {
//    var page = e.detail.page;
//    // Code for About page
//    if (page.name === 'about') {
//        // We need to get count GET parameter from URL (about.html?count=10)
//        var count = page.query.count;
//        // Now we can generate some dummy list
//        var listHTML = '<ul>';
//        for (var i = 0; i < count; i++) {
//            listHTML += '<li>' + i + '</li>';
//        }
//        listHTML += '</ul>';
//        // And insert generated list to page content
//        $$(page.container).find('.page-content').append('hello tst');
//    }
//    // Code for Services page
//    if (page.name === 'services') {
//        myApp.alert('Here comes our services!');
//    }
//});
//// Callbacks to run specific code for specific pages, for example for About page:
myApp.onPageInit('about', function (page) {
    // run createContentPage func after link was clicked
    $$('.create-page').on('click', function () {
        createContentPage();
    });
});
// Callbacks to run specific code for specific pages, for example for About page:


// Generate dynamic page
var dynamicPageIndex = 0;
function createContentPage() {
    mainView.router.loadContent(
        '<!-- Top Navbar-->' +
        '<div class="navbar">' +
        '  <div class="navbar-inner">' +
        '    <div class="left"><a href="#" class="back link"><i class="icon icon-back"></i><span>Back</span></a></div>' +
        '    <div class="center sliding">Dynamic Page ' + (++dynamicPageIndex) + '</div>' +
        '  </div>' +
        '</div>' +
        '<div class="pages">' +
        '  <!-- Page, data-page contains page name-->' +
        '  <div data-page="dynamic-pages" class="page">' +
        '    <!-- Scrollable page content-->' +
        '    <div class="page-content">' +
        '      <div class="content-block">' +
        '        <div class="content-block-inner">' +
        '          <p>Here is a dynamic page created on ' + new Date() + ' !</p>' +
        '          <p>Go <a href="#" class="back">back</a> or go to <a href="services.html">Services</a>.</p>' +
        '        </div>' +
        '      </div>' +
        '    </div>' +
        '  </div>' +
        '</div>'
    );
    return;
}