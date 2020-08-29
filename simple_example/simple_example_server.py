from concurrent import futures
import logging
import grpc
import simple_example_pb2_grpc
import simple_example_pb2


class ShoppingList(simple_example_pb2_grpc.ShoppingListServicer):

    def OrderGroceries(self, request, context):
        if request.shoppingItem == "brussel sprouts":
            return simple_example_pb2.MessageReply(inStock=True)
        else:
            return simple_example_pb2.MessageReply(inStock=False)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    simple_example_pb2_grpc.add_ShoppingListServicer_to_server(ShoppingList(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
