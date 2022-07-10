/* storage.js */
/*
封装模块 使用localStorage保存token到localStorage里，只要不删除，永久存在，实现持久化 从localStorage中取出一项数据 名字叫name（自定义名称）
*/
export const getItem = name => {
  return JSON.parse(localStorage.getItem(name))
}

/*
向localStorage中设置一项数据 名字为name里面设置值为obj
*/
export const setItem = (name, obj) => {
  localStorage.setItem(name, JSON.stringify(obj))
}

/*
删除
 */
export const removeitem = name => {
  localStorage.removeItem(name)
}
