module.exports = {
    devServer: {
      proxy: {
        "/user/": {
          target: "http://localhost:4050",
        },
        "/reserved_data/": {
          target: "http://localhost:4050",
        }
      }
    }
  };