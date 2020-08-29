import grpc
import logging
import simple_example_pb2
import simple_example_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = simple_example_pb2_grpc.ShoppingListStub(channel)
        grocery_item = "brussel sprouts"
        response = stub.OrderGroceries(simple_example_pb2.MessageRequest(shoppingItem=grocery_item))
    print("Grocery client received\n\tGrocery: " + grocery_item + "\tIn Stock:" + str(response.inStock))


if __name__ == '__main__':
    logging.basicConfig()
    run()
