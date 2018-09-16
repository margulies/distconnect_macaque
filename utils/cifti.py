import subprocess, os

def write_cifti_pscalar(data, f, dtype = 'pscalar', tpl = 'utils/template.pscalar.nii'):

    fname = '%s.pscalar.nii' % f

    assert data.shape[0] == 91, "You must have 91 vertices on the first dimension (rows)"
        
    np.savetxt('temp_data.txt',data)
    cmd = ['wb_command','-cifti-convert','-from-text','temp_data.txt', tpl, fname, '-reset-scalars']
    subprocess.call(cmd)
    os.remove('temp_data.txt')

def write_cifti_dscalar(data, f, dtype = 'dscalar', tpl = 'utils/template.dscalar.nii'):

    fname = '%s.dscalar.nii' % f
    
    assert data.shape[0] == 10242, "You must have 91 vertices on the first dimension (rows)"

    np.savetxt('temp_data.txt',data)
    cmd = ['wb_command','-cifti-convert','-from-text','temp_data.txt', tpl, fname, '-reset-scalars']
    subprocess.call(cmd)
    os.remove('temp_data.txt')
