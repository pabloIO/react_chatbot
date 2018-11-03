'use strict';

var LocalStorage = (function(){
    /**
     * @keys: [id, username, token, socket_channel, _conversation_id, sesion]
     */ 
    let keys = {};
    let _storage = window.localStorage;
    /**
     * @function setKeys    : Set all keys provided with localStorage
     * @param {Object} data : Data to save in localStorage
     */
    function setKeys(data){
        console.log(data);
        for (const key in data) {
            if (data.hasOwnProperty(key)) {
                if(key == 'success' || key == 'url_to') continue;
                setKey(key, data[key]); 
                _storage.getItem(key);
            }
        }
        // console.log(this.getKeys());
    }
    /**
     * @function setKey     : Set all keys provided with localStorage
     * @param {string}  key : Key to locate in localStorage
     * @param {string}  val : Value to set in localStorage for key
     */
    function setKey(key, val){
        _storage.setItem(key, val);
    }
    /**
     * @function getKey: Returns the value in localStorage, by the key 
     * @param {string} key: Key stored on localStorage
     * @return { string } value: Value finded in the localStorage 
     */
    function getKey(key){
        return _storage.getItem(key);
    }

    function getKeys(){
        const keys = ['id', 'username', 'token', 'socket_channel', '_conversation_id', 'sesion'];
        let data = [];
        for (let i = 0; i < keys.length; i++) {
            data.push(getKey(keys[i]));
        }
        return data;
    }

    return{
        getKey: getKey,
        getKeys: getKeys,
        setKeys: setKeys,
        setKey: setKey,
    };
})();