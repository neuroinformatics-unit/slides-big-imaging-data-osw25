import matplotlib.figure
import matplotlib.pyplot as plt
import numpy as np

def color_chunk_figure(*, image_shape: tuple[int, int, int], chunk_shape: tuple[int, int, int]) -> matplotlib.figure.Figure:
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for x in range(0, image_shape[0], chunk_shape[0]):
        for y in range(0, image_shape[1], chunk_shape[1]):
            for z in range(0, image_shape[2], chunk_shape[2]):
                voxels = np.zeros(image_shape)
                voxels[x:x+chunk_shape[0], y:y+chunk_shape[1], z:z+chunk_shape[2]] = 1
                ax.voxels(voxels, edgecolors='black', linewidths=0.5, alpha=0.9, shade=False);

    ax.set_aspect("equal")
    ax.axis('off');
    ax.set_title(f'Image shape = {image_shape}\nChunk shape = {chunk_shape}')

def transparent_figure():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    x, y, z = np.indices((10, 10, 20))

    voxels = np.ones(x.shape)
    voxels_request = (x < 4) & (x >= 2) & (y < 5) & (y >= 3) & (z < 4) & (z >= 2)
    voxels_read = (z < 4) & (z >= 2)

    all_vox = ax.voxels(voxels, alpha=0.2, edgecolors='black', linewidths=0.05, shade=False)
    req_vox = ax.voxels(voxels_request, edgecolors='black', linewidths=0.5, facecolors='tab:red', alpha=1, shade=False);
    read_vox = ax.voxels(voxels_read, edgecolors='black', linewidths=0.5, facecolors='tab:orange', alpha=0.3, shade=False);

    ax.axis('off')
    ax.set_aspect('equal')

    custom_lines = [
        list(all_vox.values())[0],
        list(req_vox.values())[0],
        list(read_vox.values())[0]]
    ax.legend(custom_lines, [
        'All data',
        f'Requested data ({np.sum(voxels_request)} voxels)',
        f'Read data ({np.sum(voxels_read)} voxels)'],
        bbox_to_anchor=(0.8, -0.1))
    ax.set_title("Chunk shape = (10, 10, 1)")

def transparent_figure_bad():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    x, y, z = np.indices((10, 10, 20))

    voxels = np.ones(x.shape)
    voxels_request = (x < 4) & (x >= 3) & (y < 4) & (y >= 3)
    voxels_read = np.ones(x.shape)

    req_vox = ax.voxels(voxels_request, edgecolors='black', linewidths=0.5, facecolors='tab:red', alpha=1, shade=False);
    read_vox = ax.voxels(voxels_read, edgecolors='black', linewidths=0.5, facecolors='tab:orange', alpha=0.3, shade=False);

    ax.axis('off')
    ax.set_aspect('equal')

    custom_lines = [
        list(req_vox.values())[0],
        list(read_vox.values())[0]]
    ax.legend(
        custom_lines,
        [
            f'Requested data ({int(np.sum(voxels_request))} voxels)',
            f'Read data ({int(np.sum(voxels_read))} voxels)'
        ],
        bbox_to_anchor=(0.8, -0.1)
    )
    ax.set_title("Chunk shape = (10, 10, 1)")

def transparent_figure_chunked():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    x, y, z = np.indices((10, 10, 20))

    voxels = np.ones(x.shape)
    voxels_request = (x < 4) & (x >= 2) & (y < 5) & (y >= 3) & (z < 4) & (z >= 2)
    voxels_read = (x < 6) & (x >= 2) & (y < 6) & (y >= 2) & (z < 6) & (z >= 0)

    all_vox = ax.voxels(voxels, alpha=0.2, edgecolors='black', linewidths=0.05, shade=False)
    req_vox = ax.voxels(voxels_request, edgecolors='black', linewidths=0.5, facecolors='tab:red', alpha=1, shade=False);
    read_vox = ax.voxels(voxels_read, edgecolors='black', linewidths=0.5, facecolors='tab:orange', alpha=0.3, shade=False);

    ax.axis('off')
    ax.set_aspect('equal')

    custom_lines = [
        list(all_vox.values())[0],
        list(req_vox.values())[0],
        list(read_vox.values())[0]]
    ax.legend(custom_lines, [
        'All data',
        f'Requested data ({np.sum(voxels_request)} voxels)',
        f'Read data ({np.sum(voxels_read)} voxels)'],
        bbox_to_anchor=(0.8, -0.1)
    )
    ax.set_title("Chunk shape = (2, 2, 3)")

def multiscale_image():
    fig = plt.figure()
    original_res = np.array([10, 10, 20])
    for i in range(3):
        ax = fig.add_subplot(1, 3, i+1, projection='3d')

        bin_factor = 2**i
        x, y, z = np.indices(np.ceil(original_res / bin_factor).astype(int).tolist())
        voxels = np.ones(x.shape)
        all_vox = ax.voxels(voxels, alpha=1, edgecolors='black', linewidths=1, shade=False)
        ax.axis('off')
        ax.set_aspect('equal')
        ax.set_title(f"Bin-by-{bin_factor}")

    fig.suptitle("OME-Zarr multiscale image arrays")
    fig.tight_layout()
    
if __name__=="__main__":
    # color_chunk_figure(image_shape=(10,10,20), chunk_shape=(10,10,1))
    # plt.savefig("img/2d-stack.png", bbox_inches="tight", dpi=300)
    # transparent_figure()
    # plt.savefig("img/2d-stack-access.png", bbox_inches="tight", dpi=300)
    # transparent_figure_bad()
    # plt.savefig("img/2d-stack-access-bad.png", bbox_inches="tight", dpi=300)
    # color_chunk_figure(image_shape=(10,10,20), chunk_shape=(2,2,3))
    # plt.savefig("img/stack-small-chunks.png", bbox_inches="tight", dpi=300)
    # color_chunk_figure(image_shape=(10,10,20), chunk_shape=(5,5,10))
    # plt.savefig("img/stack-big-chunks.png", bbox_inches="tight", dpi=300)
    # transparent_figure_chunked()
    # plt.savefig("img/chunk-access.png", bbox_inches="tight", dpi=300)
    multiscale_image()
    plt.savefig("img/multiscale.png", bbox_inches="tight", dpi=300)
    
    
