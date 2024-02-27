if __name__ == "__main__":
    # Parse the arguments
    args = parser.parse_args()
    # Load the configuration
    config.load(args.config)
    # Load the data
    data = data_load.load(args.data)
    # Load the model
    model = utils.load_model(args.model)
    # Make the predictions
    predictions = model.predict(data)
    # Save the predictions
    utils.save_predictions(predictions, args.output)
    # Start the server
    server.start()