const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = () => ({
    devtool: "nosources-source-map",
    output: {
        filename: "production.js"
    },
    optimization: {
    },
    module: {
        rules: [
            {
                test: /\.s[ac]ss$/i,
                use: [MiniCssExtractPlugin.loader, "css-loader", "sass-loader"]
            }
        ]
    },
    plugins: [new MiniCssExtractPlugin()]
});